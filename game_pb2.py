# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ngame.proto\x12\x04game\"\x1b\n\x08\x43\x61rdList\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1b\n\x08UserList\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1d\n\nCardBought\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1b\n\x08\x43\x61rdSold\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x14\n\x06IdCard\x12\n\n\x02id\x18\x01 \x01(\t\"\x07\n\x05\x45mpty2\xc2\x01\n\x0bGameService\x12,\n\x0bGetCardList\x12\x0b.game.Empty\x1a\x0e.game.CardList\"\x00\x12,\n\x0bGetUserList\x12\x0b.game.Empty\x1a\x0e.game.UserList\"\x00\x12+\n\x07\x42uyCard\x12\x0c.game.IdCard\x1a\x10.game.CardBought\"\x00\x12*\n\x08SellCard\x12\x0c.game.IdCard\x1a\x0e.game.CardSold\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'game_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_CARDLIST']._serialized_start=20
  _globals['_CARDLIST']._serialized_end=47
  _globals['_USERLIST']._serialized_start=49
  _globals['_USERLIST']._serialized_end=76
  _globals['_CARDBOUGHT']._serialized_start=78
  _globals['_CARDBOUGHT']._serialized_end=107
  _globals['_CARDSOLD']._serialized_start=109
  _globals['_CARDSOLD']._serialized_end=136
  _globals['_IDCARD']._serialized_start=138
  _globals['_IDCARD']._serialized_end=158
  _globals['_EMPTY']._serialized_start=160
  _globals['_EMPTY']._serialized_end=167
  _globals['_GAMESERVICE']._serialized_start=170
  _globals['_GAMESERVICE']._serialized_end=364
# @@protoc_insertion_point(module_scope)
