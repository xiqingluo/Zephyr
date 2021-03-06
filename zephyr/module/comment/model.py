#!/usr/bin/env python
#
# Copyright 2015-2016 zephyr
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

__all__  = ['Comment']


from datetime import datetime

class Comment(object):

    def __init__(self, post_id, name, email, content, status, created=None, cid=None):
        self.post_id = post_id
        self.name = name
        self.email = email
        self.content = content
        
        self.status = status
        self.created = created or datetime.now()
        self.cid = cid

    def __json__(self):
        return self.__dict__.copy()