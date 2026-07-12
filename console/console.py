# https://github.com/Zeronetsec/Zeronetsec

import os
import glob
from importlib import util

from utils.missing_argument import MissingArgument
from utils.invalid_option import InvalidOption

def execute(args):
    if not args or not args[0].strip():
        MissingArgument.execute()

    input_flag = args[0]
    if not input_flag.startswith('--') or input_flag == '--':
        InvalidOption.execute(input_flag)

    clean_name = input_flag[2:]
    file_name = clean_name.replace('-', '_')

    current_dir = os.path.dirname(
        os.path.abspath(__file__),
    )

    module_base_dir = os.path.abspath(
        os.path.join(current_dir, "..", "module"),
    )

    search_pattern = os.path.join(
        module_base_dir, "**", f"{file_name}.py",
    )

    matching_files = glob.glob(
        search_pattern, recursive=True,
    )

    if matching_files and os.path.exists(matching_files[0]):
        target_file = matching_files[0]
        module_name = f"dynamic_{file_name}"
        spec = util.spec_from_file_location(module_name, target_file)
        if spec is None or spec.loader is None:
            InvalidOption.execute(input_flag)

        module = util.module_from_spec(spec)
        spec.loader.exec_module(module)

        class_name = "".join([part.capitalize() for part in file_name.split('_')])
        flag_target = getattr(module, class_name, None)

        if flag_target is None:
            fallback_execute = getattr(
                module, "execute", None,
            )
            if fallback_execute and callable(fallback_execute):
                fallback_execute(args)
            else:
                InvalidOption.execute(input_flag)
                sys.exit(1)
        elif isinstance(flag_target, type):
            instance = flag_target()
            instance.execute(args)
    else:
        InvalidOption.execute(input_flag)

# Copyright (c) 2026 Zeronetsec