# Copyright © 2019 Province of British Columbia
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Manage the database and some other items required to run the API
"""
import logging

from flask_migrate import Migrate

# models included so that migrate can build the database migrations
from api import create_app
from api.models import db
from flask.cli import FlaskGroup


APP = create_app(run_mode='migration')
cli = FlaskGroup(APP)


MIGRATE = Migrate(APP, db)

if __name__ == '__main__':
    logging.log(logging.INFO, 'Running the Manager')
    cli()