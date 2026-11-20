#pragma once
#ifndef CPPTEX_HPP
#define CPPTEX_HPP

#ifdef __cplusplus
extern "C" {
#endif

#include <stddef.h>
#include <stdio.h>

typedef struct texobj* texptr;

void delete_texobj(texobj *);

texptr tex_newvar(const char *name);
texptr tex_newint(int n);
texptr tex_sum(texptr terms, int n);
texptr tex_product(texptr terms, int n);
texptr tex_exponent(texptr base, texptr exponent);

texptr tex_trig_sin(texptr nested);
texptr tex_trig_cos(texptr nested);
texptr tex_trig_tan(texptr nested);
texptr tex_trig_sec(texptr nested);
texptr tex_trig_csc(texptr nested);
texptr tex_trig_cot(texptr nested);

texptr tex_derivative(texptr expr, texptr var, int count);

struct texformat;
texformat *new_texformat();
// TODO
typedef void (*texstream)(void * ctx, int n); // A function that reads n characters from the passed buffer
int tex_chunkwrite(texformat *fmt, texptr obj, char *buf, int buflen, texstream bufclear, void *ctx);

#ifdef __cplusplus
}
#endif

#endif
