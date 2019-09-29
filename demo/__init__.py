# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals


import python_atom_sdk


def demo():
    """
    @summary: demo
    """
    python_atom_sdk.log.info("enter demo")

    # 输入
    input_params = python_atom_sdk.get_input()
    # print("插件入参：", input_params)
    # 插件逻辑
    print("Hello world!")

    # 插件执行结果、输出数据
    output_data = {
        "status": python_atom_sdk.status.SUCCESS,
        "message": "run succ",
        "type": python_atom_sdk.output_template_type.DEFAULT,
        "data": {
            "outputDemo": {
                "type": python_atom_sdk.output_field_type.STRING,
                "value": "test output"
            }
        }
    }
    python_atom_sdk.set_output(output_data)

    python_atom_sdk.log.info("finish")

    exit(0)  # 无错误退出 exit(1)有错误退出
