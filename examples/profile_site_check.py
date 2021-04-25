# -*- coding: utf-8 -*-
import requests
import cProfile
 
 
def facebook():
    requests.get('https://facebook.com')
 
 
def google():
    requests.get('https://google.com')
def twitter():
    requests.get('https://twitter.com')
def vk():
    requests.get('https://vk.com')
 
 
def main():
    facebook()
    google()
    twitter()
    vk()
cProfile.run('main()')