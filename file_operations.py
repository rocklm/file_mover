'''
===================================================================
Script: 
File Operations

Purpose:
simple functions to move, copy and delete files and folders

Notes:
(1) N/A

===================================================================
'''

import os
import shutil


def move_files(current_path, target_path, file_names):
    for file in file_names:
        old_loc = current_path + '\\' + file
        new_loc = target_path + '\\' + file
        shutil.move(old_loc, new_loc)
        
                          
def copy_files(current_path, target_path, file_names):
        for file in file_names:
            old_loc = current_path + '\\' + file
            new_loc = target_path + '\\' + file
            shutil.copy(old_loc, new_loc)


def delete_files(target_path, file_names):
    for file in file_names:
         delete_path =  target_path + '\\' + file
         os.remove(delete_path)


def move_folder(current_path, target_path):
    os.rename(current_path, target_path) 


def copy_folder(current_path, target_path):
    shutil.copytree(current_path, target_path) 
       
def delete_folder(path):
    shutil.rmtree(path) 
    
    

