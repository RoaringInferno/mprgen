#pragma once

#include "generate/math-problem.hpp"
#include "generate/number.hpp"

#include <cstdint>
#include <vector>

namespace generate
{
    typedef uint32_t problem_count_t;
    typedef std::vector<mprgen::MathProblem> vector_t;
    typedef std::vector<mprgen::MathProblem>::iterator problem_iterator_t;

    typedef struct {
        problem_iterator_t begin;
        problem_iterator_t end;
    } iterator_range_t;

    iterator_range_t iterator_range(vector_t& range);
};