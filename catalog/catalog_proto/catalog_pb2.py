# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: catalog.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='catalog.proto',
  package='catalog',
  syntax='proto3',
  serialized_pb=_b('\n\rcatalog.proto\x12\x07\x63\x61talog\")\n\x04Item\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"\x1b\n\x0bItemRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"-\n\x0eSetItemRequest\x12\x1b\n\x04item\x18\x01 \x01(\x0b\x32\r.catalog.Item\"+\n\x0cItemResponse\x12\x1b\n\x04item\x18\x01 \x01(\x0b\x32\r.catalog.Item\"\x1d\n\x0cItemsRequest\x12\r\n\x05names\x18\x01 \x03(\t\"/\n\x0fSetItemsRequest\x12\x1c\n\x05items\x18\x01 \x03(\x0b\x32\r.catalog.Item\"-\n\rItemsResponse\x12\x1c\n\x05items\x18\x01 \x03(\x0b\x32\r.catalog.Item2\x99\x04\n\x0e\x43\x61talogManager\x12\x38\n\x07GetItem\x12\x14.catalog.ItemRequest\x1a\x15.catalog.ItemResponse\"\x00\x12;\n\x07SetItem\x12\x17.catalog.SetItemRequest\x1a\x15.catalog.ItemResponse\"\x00\x12;\n\nDeleteItem\x12\x14.catalog.ItemRequest\x1a\x15.catalog.ItemResponse\"\x00\x12;\n\x08GetItems\x12\x15.catalog.ItemsRequest\x1a\x16.catalog.ItemsResponse\"\x00\x12>\n\x08SetItems\x12\x18.catalog.SetItemsRequest\x1a\x16.catalog.ItemsResponse\"\x00\x12>\n\x0b\x44\x65leteItems\x12\x15.catalog.ItemsRequest\x1a\x16.catalog.ItemsResponse\"\x00\x12\x44\n\x10GetItemsAsStream\x12\x15.catalog.ItemsRequest\x1a\x15.catalog.ItemResponse\"\x00\x30\x01\x12P\n\x1bGetItemsAsStreamInteractive\x12\x14.catalog.ItemRequest\x1a\x15.catalog.ItemResponse\"\x00(\x01\x30\x01\x42\x39Z7github.com/dknlam/grpc_playground/catalog/catalog_protob\x06proto3')
)




_ITEM = _descriptor.Descriptor(
  name='Item',
  full_name='catalog.Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='catalog.Item.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='catalog.Item.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=67,
)


_ITEMREQUEST = _descriptor.Descriptor(
  name='ItemRequest',
  full_name='catalog.ItemRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='catalog.ItemRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=96,
)


_SETITEMREQUEST = _descriptor.Descriptor(
  name='SetItemRequest',
  full_name='catalog.SetItemRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='catalog.SetItemRequest.item', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=98,
  serialized_end=143,
)


_ITEMRESPONSE = _descriptor.Descriptor(
  name='ItemResponse',
  full_name='catalog.ItemResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='catalog.ItemResponse.item', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=145,
  serialized_end=188,
)


_ITEMSREQUEST = _descriptor.Descriptor(
  name='ItemsRequest',
  full_name='catalog.ItemsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='names', full_name='catalog.ItemsRequest.names', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=190,
  serialized_end=219,
)


_SETITEMSREQUEST = _descriptor.Descriptor(
  name='SetItemsRequest',
  full_name='catalog.SetItemsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='catalog.SetItemsRequest.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=221,
  serialized_end=268,
)


_ITEMSRESPONSE = _descriptor.Descriptor(
  name='ItemsResponse',
  full_name='catalog.ItemsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='catalog.ItemsResponse.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=270,
  serialized_end=315,
)

_SETITEMREQUEST.fields_by_name['item'].message_type = _ITEM
_ITEMRESPONSE.fields_by_name['item'].message_type = _ITEM
_SETITEMSREQUEST.fields_by_name['items'].message_type = _ITEM
_ITEMSRESPONSE.fields_by_name['items'].message_type = _ITEM
DESCRIPTOR.message_types_by_name['Item'] = _ITEM
DESCRIPTOR.message_types_by_name['ItemRequest'] = _ITEMREQUEST
DESCRIPTOR.message_types_by_name['SetItemRequest'] = _SETITEMREQUEST
DESCRIPTOR.message_types_by_name['ItemResponse'] = _ITEMRESPONSE
DESCRIPTOR.message_types_by_name['ItemsRequest'] = _ITEMSREQUEST
DESCRIPTOR.message_types_by_name['SetItemsRequest'] = _SETITEMSREQUEST
DESCRIPTOR.message_types_by_name['ItemsResponse'] = _ITEMSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Item = _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), dict(
  DESCRIPTOR = _ITEM,
  __module__ = 'catalog_pb2'
  # @@protoc_insertion_point(class_scope:catalog.Item)
  ))
_sym_db.RegisterMessage(Item)

ItemRequest = _reflection.GeneratedProtocolMessageType('ItemRequest', (_message.Message,), dict(
  DESCRIPTOR = _ITEMREQUEST,
  __module__ = 'catalog_pb2'
  # @@protoc_insertion_point(class_scope:catalog.ItemRequest)
  ))
_sym_db.RegisterMessage(ItemRequest)

SetItemRequest = _reflection.GeneratedProtocolMessageType('SetItemRequest', (_message.Message,), dict(
  DESCRIPTOR = _SETITEMREQUEST,
  __module__ = 'catalog_pb2'
  # @@protoc_insertion_point(class_scope:catalog.SetItemRequest)
  ))
_sym_db.RegisterMessage(SetItemRequest)

ItemResponse = _reflection.GeneratedProtocolMessageType('ItemResponse', (_message.Message,), dict(
  DESCRIPTOR = _ITEMRESPONSE,
  __module__ = 'catalog_pb2'
  # @@protoc_insertion_point(class_scope:catalog.ItemResponse)
  ))
_sym_db.RegisterMessage(ItemResponse)

ItemsRequest = _reflection.GeneratedProtocolMessageType('ItemsRequest', (_message.Message,), dict(
  DESCRIPTOR = _ITEMSREQUEST,
  __module__ = 'catalog_pb2'
  # @@protoc_insertion_point(class_scope:catalog.ItemsRequest)
  ))
_sym_db.RegisterMessage(ItemsRequest)

SetItemsRequest = _reflection.GeneratedProtocolMessageType('SetItemsRequest', (_message.Message,), dict(
  DESCRIPTOR = _SETITEMSREQUEST,
  __module__ = 'catalog_pb2'
  # @@protoc_insertion_point(class_scope:catalog.SetItemsRequest)
  ))
_sym_db.RegisterMessage(SetItemsRequest)

ItemsResponse = _reflection.GeneratedProtocolMessageType('ItemsResponse', (_message.Message,), dict(
  DESCRIPTOR = _ITEMSRESPONSE,
  __module__ = 'catalog_pb2'
  # @@protoc_insertion_point(class_scope:catalog.ItemsResponse)
  ))
_sym_db.RegisterMessage(ItemsResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z7github.com/dknlam/grpc_playground/catalog/catalog_proto'))

_CATALOGMANAGER = _descriptor.ServiceDescriptor(
  name='CatalogManager',
  full_name='catalog.CatalogManager',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=318,
  serialized_end=855,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetItem',
    full_name='catalog.CatalogManager.GetItem',
    index=0,
    containing_service=None,
    input_type=_ITEMREQUEST,
    output_type=_ITEMRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetItem',
    full_name='catalog.CatalogManager.SetItem',
    index=1,
    containing_service=None,
    input_type=_SETITEMREQUEST,
    output_type=_ITEMRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteItem',
    full_name='catalog.CatalogManager.DeleteItem',
    index=2,
    containing_service=None,
    input_type=_ITEMREQUEST,
    output_type=_ITEMRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetItems',
    full_name='catalog.CatalogManager.GetItems',
    index=3,
    containing_service=None,
    input_type=_ITEMSREQUEST,
    output_type=_ITEMSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetItems',
    full_name='catalog.CatalogManager.SetItems',
    index=4,
    containing_service=None,
    input_type=_SETITEMSREQUEST,
    output_type=_ITEMSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteItems',
    full_name='catalog.CatalogManager.DeleteItems',
    index=5,
    containing_service=None,
    input_type=_ITEMSREQUEST,
    output_type=_ITEMSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetItemsAsStream',
    full_name='catalog.CatalogManager.GetItemsAsStream',
    index=6,
    containing_service=None,
    input_type=_ITEMSREQUEST,
    output_type=_ITEMRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetItemsAsStreamInteractive',
    full_name='catalog.CatalogManager.GetItemsAsStreamInteractive',
    index=7,
    containing_service=None,
    input_type=_ITEMREQUEST,
    output_type=_ITEMRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CATALOGMANAGER)

DESCRIPTOR.services_by_name['CatalogManager'] = _CATALOGMANAGER

# @@protoc_insertion_point(module_scope)
