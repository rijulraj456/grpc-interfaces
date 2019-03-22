# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import cartesi_base_pb2 as cartesi__base__pb2
import manager_high_pb2 as manager__high__pb2


class MachineManagerHighStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.NewSession = channel.unary_unary(
        '/CartesiManagerHigh.MachineManagerHigh/NewSession',
        request_serializer=manager__high__pb2.NewSessionRequest.SerializeToString,
        response_deserializer=cartesi__base__pb2.Hash.FromString,
        )
    self.SessionRun = channel.unary_unary(
        '/CartesiManagerHigh.MachineManagerHigh/SessionRun',
        request_serializer=manager__high__pb2.SessionRunRequest.SerializeToString,
        response_deserializer=manager__high__pb2.SessionRunResult.FromString,
        )
    self.SessionStep = channel.unary_unary(
        '/CartesiManagerHigh.MachineManagerHigh/SessionStep',
        request_serializer=manager__high__pb2.SessionStepRequest.SerializeToString,
        response_deserializer=manager__high__pb2.SessionStepResult.FromString,
        )


class MachineManagerHighServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def NewSession(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SessionRun(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SessionStep(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MachineManagerHighServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'NewSession': grpc.unary_unary_rpc_method_handler(
          servicer.NewSession,
          request_deserializer=manager__high__pb2.NewSessionRequest.FromString,
          response_serializer=cartesi__base__pb2.Hash.SerializeToString,
      ),
      'SessionRun': grpc.unary_unary_rpc_method_handler(
          servicer.SessionRun,
          request_deserializer=manager__high__pb2.SessionRunRequest.FromString,
          response_serializer=manager__high__pb2.SessionRunResult.SerializeToString,
      ),
      'SessionStep': grpc.unary_unary_rpc_method_handler(
          servicer.SessionStep,
          request_deserializer=manager__high__pb2.SessionStepRequest.FromString,
          response_serializer=manager__high__pb2.SessionStepResult.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'CartesiManagerHigh.MachineManagerHigh', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))