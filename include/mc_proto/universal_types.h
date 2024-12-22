#pragma once

#include <stddef.h>
#include <stdint.h>

typedef char* mc_proto_str;

typedef struct {
	uint8_t* data;
	size_t len;
	size_t pos;
} mc_proto_buffer;

typedef int32_t mc_proto_varint;
typedef int64_t mc_proto_varlong;
