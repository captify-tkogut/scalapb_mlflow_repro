# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: scalapb.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rscalapb.proto\x12\x07scalapb\x1a google/protobuf/descriptor.proto\"\x82\x03\n\x0eScalaPbOptions\x12\x14\n\x0cpackage_name\x18\x01 \x01(\t\x12\x14\n\x0c\x66lat_package\x18\x02 \x01(\x08\x12\x0e\n\x06import\x18\x03 \x03(\t\x12\x10\n\x08preamble\x18\x04 \x03(\t\x12\x13\n\x0bsingle_file\x18\x05 \x01(\x08\x12\x1d\n\x15no_primitive_wrappers\x18\x07 \x01(\x08\x12\x1a\n\x12primitive_wrappers\x18\x06 \x01(\x08\x12\x17\n\x0f\x63ollection_type\x18\x08 \x01(\t\x12\x1f\n\x17preserve_unknown_fields\x18\t \x01(\x08\x12\x13\n\x0bobject_name\x18\n \x01(\t\x12\x33\n\x05scope\x18\x0b \x01(\x0e\x32$.scalapb.ScalaPbOptions.OptionsScope\x12\'\n\x1dtest_only_no_java_conversions\x18\xa1\x8d\x06 \x01(\x08\"%\n\x0cOptionsScope\x12\x08\n\x04\x46ILE\x10\x00\x12\x0b\n\x07PACKAGE\x10\x01\"~\n\x0eMessageOptions\x12\x0f\n\x07\x65xtends\x18\x01 \x03(\t\x12\x19\n\x11\x63ompanion_extends\x18\x02 \x03(\t\x12\x13\n\x0b\x61nnotations\x18\x03 \x03(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\x1d\n\x15\x63ompanion_annotations\x18\x05 \x03(\t\"\x94\x01\n\x0c\x46ieldOptions\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x12\n\nscala_name\x18\x02 \x01(\t\x12\x17\n\x0f\x63ollection_type\x18\x03 \x01(\t\x12\x10\n\x08key_type\x18\x04 \x01(\t\x12\x12\n\nvalue_type\x18\x05 \x01(\t\x12\x13\n\x0b\x61nnotations\x18\x06 \x03(\t\x12\x0e\n\x06no_box\x18\x1e \x01(\x08\"G\n\x0b\x45numOptions\x12\x0f\n\x07\x65xtends\x18\x01 \x03(\t\x12\x19\n\x11\x63ompanion_extends\x18\x02 \x03(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\"#\n\x10\x45numValueOptions\x12\x0f\n\x07\x65xtends\x18\x01 \x03(\t\"\x1f\n\x0cOneofOptions\x12\x0f\n\x07\x65xtends\x18\x01 \x03(\t:G\n\x07options\x12\x1c.google.protobuf.FileOptions\x18\xfc\x07 \x01(\x0b\x32\x17.scalapb.ScalaPbOptions:J\n\x07message\x12\x1f.google.protobuf.MessageOptions\x18\xfc\x07 \x01(\x0b\x32\x17.scalapb.MessageOptions:D\n\x05\x66ield\x12\x1d.google.protobuf.FieldOptions\x18\xfc\x07 \x01(\x0b\x32\x15.scalapb.FieldOptions:I\n\x0c\x65num_options\x12\x1c.google.protobuf.EnumOptions\x18\xfc\x07 \x01(\x0b\x32\x14.scalapb.EnumOptions:Q\n\nenum_value\x12!.google.protobuf.EnumValueOptions\x18\xfc\x07 \x01(\x0b\x32\x19.scalapb.EnumValueOptions:D\n\x05oneof\x12\x1d.google.protobuf.OneofOptions\x18\xfc\x07 \x01(\x0b\x32\x15.scalapb.OneofOptionsB\'\n\x0fscalapb.options\xe2?\x13\n\x0fscalapb.options\x10\x01')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'scalapb_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
  google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(options)
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(message)
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(field)
  google_dot_protobuf_dot_descriptor__pb2.EnumOptions.RegisterExtension(enum_options)
  google_dot_protobuf_dot_descriptor__pb2.EnumValueOptions.RegisterExtension(enum_value)
  google_dot_protobuf_dot_descriptor__pb2.OneofOptions.RegisterExtension(oneof)

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\017scalapb.options\342?\023\n\017scalapb.options\020\001'
  _SCALAPBOPTIONS._serialized_start=61
  _SCALAPBOPTIONS._serialized_end=447
  _SCALAPBOPTIONS_OPTIONSSCOPE._serialized_start=410
  _SCALAPBOPTIONS_OPTIONSSCOPE._serialized_end=447
  _MESSAGEOPTIONS._serialized_start=449
  _MESSAGEOPTIONS._serialized_end=575
  _FIELDOPTIONS._serialized_start=578
  _FIELDOPTIONS._serialized_end=726
  _ENUMOPTIONS._serialized_start=728
  _ENUMOPTIONS._serialized_end=799
  _ENUMVALUEOPTIONS._serialized_start=801
  _ENUMVALUEOPTIONS._serialized_end=836
  _ONEOFOPTIONS._serialized_start=838
  _ONEOFOPTIONS._serialized_end=869
# @@protoc_insertion_point(module_scope)