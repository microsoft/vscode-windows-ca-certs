#include <Windows.h>
#include <Wincrypt.h>
#include <napi.h>

class Crypt32 : public Napi::ObjectWrap<Crypt32> {
 public:
  static Napi::Object Init(Napi::Env, Napi::Object);
  Crypt32(const Napi::CallbackInfo& info);

 private:
  HCERTSTORE hStore;
  PCCERT_CONTEXT pCtx = nullptr;

  static HCERTSTORE openStore(const Napi::CallbackInfo&);

  Napi::Value next(const Napi::CallbackInfo&);
  Napi::Value done(const Napi::CallbackInfo&);
  Napi::Value none(const Napi::CallbackInfo&);

  const uint8_t* begin() const { return pCtx->pbCertEncoded; }
  const uint8_t* end() const { return begin() + pCtx->cbCertEncoded; }
};

// Implementation

Crypt32::Crypt32(const Napi::CallbackInfo& info)
    : Napi::ObjectWrap<Crypt32>(info), hStore(openStore(info)) {}

HCERTSTORE Crypt32::openStore(const Napi::CallbackInfo& info) {
  return CertOpenSystemStoreA(
      0, info.Length() > 0 && info[0].IsString()
             ? info[0].As<Napi::String>().Utf8Value().c_str()
             : "ROOT");
}

Napi::Value Crypt32::next(const Napi::CallbackInfo& info) {
  if (!hStore) return done(info);
  return (pCtx = CertEnumCertificatesInStore(hStore, pCtx))
             ? Napi::Buffer<uint8_t>::Copy(info.Env(), begin(),
                                           pCtx->cbCertEncoded)
             : done(info);
}

Napi::Value Crypt32::done(const Napi::CallbackInfo& info) {
  if (hStore) CertCloseStore(hStore, 0);
  hStore = 0;
  return info.Env().Undefined();
}

Napi::Value Crypt32::none(const Napi::CallbackInfo& info) {
  return Napi::Boolean::New(info.Env(), !hStore);
}

Napi::Object Crypt32::Init(Napi::Env env, Napi::Object exports) {
  Napi::Function func = DefineClass(
      env, "Crypt32",
      {
          InstanceMethod<&Crypt32::done>("done"),
          InstanceMethod<&Crypt32::next>("next"),
          InstanceMethod<&Crypt32::none>("none"),
      });

  Napi::FunctionReference* constructor = new Napi::FunctionReference();
  *constructor = Napi::Persistent(func);
  exports.Set("Crypt32", func);
  env.SetInstanceData<Napi::FunctionReference>(constructor);

  return exports;
}

// Initialize native add-on
Napi::Object Init(Napi::Env env, Napi::Object exports) {
  Crypt32::Init(env, exports);
  return exports;
}

NODE_API_MODULE(NODE_GYP_MODULE_NAME, Init)
