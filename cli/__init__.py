"""
Initialization file for the command-line interface package.
"""

from .ansi import (
    BG_COLORS_16,
    BG_COLORS_256,
    COLORS_16,
    COLORS_256,
    RESET,
    TEXT_ATTRIBUTES,
    background_color_16,
    background_color_256,
    foreground_color_16,
    foreground_color_256,
    text_attribute
)

from .cli_program import CLIProgram
from .constants import *

from .ini import (
    get_bool_option,
    get_float_option,
    get_int_option,
    get_json_option,
    get_str_option,
    get_str_option_with_fallback,
    get_str_options,
    has_defaults,
    has_sections,
    is_empty,
    read_options
)

from .io import (
    FileInfo,
    print_normalized_line,
    read_text_files,
    write_text_to_file
)

from .patterns import (
    color_pattern_matches,
    compile_combined_patterns,
    compile_patterns,
    matches_all_patterns
)

from .terminal import (
    input_is_redirected,
    input_is_terminal,
    output_is_terminal
)

from .types import (
    ErrorReporter,
    Json,
    Patterns
)
