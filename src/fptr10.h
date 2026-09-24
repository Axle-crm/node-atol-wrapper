#ifndef INCLUDE_Fptr10
#define INCLUDE_Fptr10

#include "wcast_disable.h"

DISABLE_WCAST_FUNCTION_TYPE
#include <nan.h>
DISABLE_WCAST_FUNCTION_TYPE_END
#include <vector>
#include "json_worker.h"
#include "libfptr10.h"

class JsonWorker;

class Fptr10 : public Nan::ObjectWrap {
public:
  libfptr_handle fptr;
  double x;
  bool jsonAsyncTaskIsRunning = false;
  std::deque<JsonWorker*> taskQueue;

  static NAN_MODULE_INIT(Init);
  static NAN_METHOD(New);

  static NAN_METHOD(IsOpened);
  static NAN_METHOD(Create);
  static NAN_METHOD(Destroy);
  static NAN_METHOD(GetSettings);
  static NAN_METHOD(SetSettings);
  static NAN_METHOD(Open);
  static NAN_METHOD(Close);

  static NAN_METHOD(ProcessJsonAsync);
  static NAN_METHOD(ProcessJson);
  static NAN_METHOD(FnReport);
  static NAN_METHOD(FindLastDocument);

  static NAN_METHOD(SetParam);
  static NAN_METHOD(GetParamInt);
  static NAN_METHOD(GetParamBool);
  static NAN_METHOD(GetParamDouble);
  static NAN_METHOD(GetParamStr);
  static NAN_METHOD(GetParamByteArray);
  static NAN_METHOD(GetParamDatetime);
  static NAN_METHOD(ResetParams);
  static NAN_METHOD(ErrorCode);
  static NAN_METHOD(ErrorDescription);
  static NAN_METHOD(ResetError);

  static NAN_METHOD(OperatorLogin);
  static NAN_METHOD(QueryData);
  static NAN_METHOD(FnQueryData);
  static NAN_METHOD(OpenShift);
  static NAN_METHOD(Report);
  static NAN_METHOD(OpenReceipt);
  static NAN_METHOD(CancelReceipt);
  static NAN_METHOD(CloseReceipt);
  static NAN_METHOD(CheckDocumentClosed);
  static NAN_METHOD(ContinuePrint);
  static NAN_METHOD(Registration);
  static NAN_METHOD(Payment);
  static NAN_METHOD(ReceiptTotal);
  static NAN_METHOD(BeginNonfiscalDocument);
  static NAN_METHOD(EndNonfiscalDocument);
  static NAN_METHOD(PrintText);
  static NAN_METHOD(PrintBarcode);
  static NAN_METHOD(BeginMarkingCodeValidation);
  static NAN_METHOD(GetMarkingCodeValidationStatus);
  static NAN_METHOD(CancelMarkingCodeValidation);
  static NAN_METHOD(AcceptMarkingCode);
  static NAN_METHOD(DeclineMarkingCode);
  static NAN_METHOD(ReadDeviceSetting);
  static NAN_METHOD(WriteDeviceSetting);
  static NAN_METHOD(UtilFormTlv);
  static NAN_METHOD(UtilFormNomenclature);

  static NAN_GETTER(HandleGetters);
  static NAN_SETTER(HandleSetters);

  static Nan::Persistent<v8::FunctionTemplate> constructor;
  static void workerFinished(Fptr10* self);
};

#endif
