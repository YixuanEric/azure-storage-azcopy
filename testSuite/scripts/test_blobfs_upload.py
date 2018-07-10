import json
import os
import shutil
from collections import namedtuple
from stat import *
import sys
import utility as util
import unittest

class BlobFs_Upload_User_Scenarios(unittest.TestCase):

    def test_blobfs_upload_1Kb_file(self):
        # create file of size 1KB
        filename = "test_blob_1kb_file.txt"
        file_path = util.create_test_file(filename, 1024)
        # upload the file using Azcopy
        result = util.Command("copy").add_arguments(file_path).add_arguments(util.test_bfs_account_url).\
                    add_flags("log-level", "Info").execute_azcopy_copy_command()
        self.assertTrue(result)

        # Validate the file uploaded file
        fileUrl = util.test_bfs_account_url + filename
        result = util.Command("testBlobFS").add_arguments(file_path).add_arguments(fileUrl).execute_azcopy_verify()
        self.assertTrue(result)

    def test_blobfs_upload_64MB_file(self):
        # create test file of size 64MB
        filename = "test_blob_64MB_file.txt"
        file_path = util.create_test_file(filename, 64*1024*1024)
        # Upload the file using Azcopy
        result = util.Command("copy").add_arguments(file_path).add_arguments(util.test_bfs_account_url). \
            add_flags("log-level", "Info").execute_azcopy_copy_command()
        self.assertTrue(result)

        # Validate the file uploaded
        fileUrl = util.test_bfs_account_url + filename
        result = util.Command("testBlobFS").add_arguments(file_path).add_arguments(fileUrl).execute_azcopy_verify()
        self.assertTrue(result)


    def test_blobfs_upload_100_1Kb_file(self):
        # create dir with 100 1KB files inside it
        dir_name = "dir_blobfs_100_1K"
        dir_n_file_path = util.create_test_n_files(1024, 100, dir_name)

        # Upload the directory with 100 files inside it
        result = util.Command("copy").add_arguments(dir_n_file_path).add_arguments(util.test_bfs_account_url). \
            add_flags("log-level", "Info").add_flags("recursive","true").execute_azcopy_copy_command()
        self.assertTrue(result)

        # Validate the uploaded directory
        dirUrl = util.test_bfs_account_url + dir_name
        result = util.Command("testBlobFS").add_arguments(dir_n_file_path).add_arguments(dirUrl).\
                    add_flags("is-object-dir", "true").execute_azcopy_verify()
        self.assertTrue(result)

    def test_blobfs_upload_200_1Kb_file(self):
        # create dir with 100 1KB files inside it
        dir_name = "dir_blobfs_200_1K"
        dir_n_file_path = util.create_test_n_files(1024, 200, dir_name)

        # Upload the directory with 2000 files inside it
        result = util.Command("copy").add_arguments(dir_n_file_path).add_arguments(util.test_bfs_account_url). \
            add_flags("log-level", "Info").add_flags("recursive","true").execute_azcopy_copy_command()
        self.assertTrue(result)

        # Validate the uploaded directory
        dirUrl = util.test_bfs_account_url + dir_name
        result = util.Command("testBlobFS").add_arguments(dir_n_file_path).add_arguments(dirUrl). \
            add_flags("is-object-dir", "true").execute_azcopy_verify()
        self.assertTrue(result)