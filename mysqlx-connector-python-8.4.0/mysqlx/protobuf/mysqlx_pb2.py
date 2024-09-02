# -*- coding: utf-8 -*-
# Copyright (c) 2017, 2024, Oracle and/or its affiliates.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License, version 2.0, as
# published by the Free Software Foundation.
#
# This program is designed to work with certain software (including
# but not limited to OpenSSL) that is licensed under separate terms,
# as designated in a particular file or component or in included license
# documentation. The authors of MySQL hereby grant you an
# additional permission to link the program and your derivative works
# with the separately licensed software that they have either included with
# the program or referenced in the documentation.
#
# Without limiting anything contained in the foregoing, this file,
# which is part of MySQL Connector/Python, is also subject to the
# Universal FOSS Exception, version 1.0, a copy of which can be found at
# http://oss.oracle.com/licenses/universal-foss-exception.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License, version 2.0, for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin St, Fifth Floor, Boston, MA 02110-1301  USA

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mysqlx.proto

# type: ignore

"""Generated protocol buffer code."""
from google.protobuf import (
    descriptor as _descriptor,
    descriptor_pool as _descriptor_pool,
    symbol_database as _symbol_database,
)
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0cmysqlx.proto\x12\x06Mysqlx"\xfc\x03\n\x0e\x43lientMessages"\xe9\x03\n\x04Type\x12\x18\n\x14\x43ON_CAPABILITIES_GET\x10\x01\x12\x18\n\x14\x43ON_CAPABILITIES_SET\x10\x02\x12\r\n\tCON_CLOSE\x10\x03\x12\x1b\n\x17SESS_AUTHENTICATE_START\x10\x04\x12\x1e\n\x1aSESS_AUTHENTICATE_CONTINUE\x10\x05\x12\x0e\n\nSESS_RESET\x10\x06\x12\x0e\n\nSESS_CLOSE\x10\x07\x12\x14\n\x10SQL_STMT_EXECUTE\x10\x0c\x12\r\n\tCRUD_FIND\x10\x11\x12\x0f\n\x0b\x43RUD_INSERT\x10\x12\x12\x0f\n\x0b\x43RUD_UPDATE\x10\x13\x12\x0f\n\x0b\x43RUD_DELETE\x10\x14\x12\x0f\n\x0b\x45XPECT_OPEN\x10\x18\x12\x10\n\x0c\x45XPECT_CLOSE\x10\x19\x12\x14\n\x10\x43RUD_CREATE_VIEW\x10\x1e\x12\x14\n\x10\x43RUD_MODIFY_VIEW\x10\x1f\x12\x12\n\x0e\x43RUD_DROP_VIEW\x10 \x12\x13\n\x0fPREPARE_PREPARE\x10(\x12\x13\n\x0fPREPARE_EXECUTE\x10)\x12\x16\n\x12PREPARE_DEALLOCATE\x10*\x12\x0f\n\x0b\x43URSOR_OPEN\x10+\x12\x10\n\x0c\x43URSOR_CLOSE\x10,\x12\x10\n\x0c\x43URSOR_FETCH\x10-\x12\x0f\n\x0b\x43OMPRESSION\x10."\xf3\x02\n\x0eServerMessages"\xe0\x02\n\x04Type\x12\x06\n\x02OK\x10\x00\x12\t\n\x05\x45RROR\x10\x01\x12\x15\n\x11\x43ONN_CAPABILITIES\x10\x02\x12\x1e\n\x1aSESS_AUTHENTICATE_CONTINUE\x10\x03\x12\x18\n\x14SESS_AUTHENTICATE_OK\x10\x04\x12\n\n\x06NOTICE\x10\x0b\x12\x1e\n\x1aRESULTSET_COLUMN_META_DATA\x10\x0c\x12\x11\n\rRESULTSET_ROW\x10\r\x12\x18\n\x14RESULTSET_FETCH_DONE\x10\x0e\x12\x1d\n\x19RESULTSET_FETCH_SUSPENDED\x10\x0f\x12(\n$RESULTSET_FETCH_DONE_MORE_RESULTSETS\x10\x10\x12\x17\n\x13SQL_STMT_EXECUTE_OK\x10\x11\x12(\n$RESULTSET_FETCH_DONE_MORE_OUT_PARAMS\x10\x12\x12\x0f\n\x0b\x43OMPRESSION\x10\x13"\x11\n\x02Ok\x12\x0b\n\x03msg\x18\x01 \x01(\t"\x88\x01\n\x05\x45rror\x12/\n\x08severity\x18\x01 \x01(\x0e\x32\x16.Mysqlx.Error.Severity:\x05\x45RROR\x12\x0c\n\x04\x63ode\x18\x02 \x02(\r\x12\x11\n\tsql_state\x18\x04 \x02(\t\x12\x0b\n\x03msg\x18\x03 \x02(\t" \n\x08Severity\x12\t\n\x05\x45RROR\x10\x00\x12\t\n\x05\x46\x41TAL\x10\x01\x42\x1b\n\x17\x63om.mysql.cj.x.protobufH\x03'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "mysqlx_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\027com.mysql.cj.x.protobufH\003"
    _CLIENTMESSAGES._serialized_start = 25
    _CLIENTMESSAGES._serialized_end = 533
    _CLIENTMESSAGES_TYPE._serialized_start = 44
    _CLIENTMESSAGES_TYPE._serialized_end = 533
    _SERVERMESSAGES._serialized_start = 536
    _SERVERMESSAGES._serialized_end = 907
    _SERVERMESSAGES_TYPE._serialized_start = 555
    _SERVERMESSAGES_TYPE._serialized_end = 907
    _OK._serialized_start = 909
    _OK._serialized_end = 926
    _ERROR._serialized_start = 929
    _ERROR._serialized_end = 1065
    _ERROR_SEVERITY._serialized_start = 1033
    _ERROR_SEVERITY._serialized_end = 1065
# @@protoc_insertion_point(module_scope)
