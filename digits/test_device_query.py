# Copyright (c) 2015, NVIDIA CORPORATION.  All rights reserved.

import os
import mock
import unittest
import platform

from . import device_query as _

class TestGetDevices():
    """
    tests for device_query.get_devices()
    """

    @unittest.skipIf(platform.system() not in ['Linux', 'Darwin'],
            'Platform not supported')
    @mock.patch('digits.device_query.ctypes.cdll')
    def test_no_cudart(self, mock_cdll):
        """test no cudart"""
        mock_cdll.LoadLibrary.return_value = None
        assert _.get_devices(True) == [], 'Devices found even when CUDA disabled!'


class TestGetNvmlInfo():
    """
    tests for device_query.get_nvml_info()
    """

    @unittest.skipIf(len(_.get_devices(True)) == 0,
            'No GPUs on system')
    def test_memory_info_exists(self):
        for index, device in enumerate(_.get_devices(True)):
            assert 'memory' in _.get_nvml_info(index), 'NVML should have memory information for "%s"' % device.name


