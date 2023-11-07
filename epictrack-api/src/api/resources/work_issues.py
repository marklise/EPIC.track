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
"""Resource for work issues endpoints."""
from http import HTTPStatus

from flask import jsonify
from flask_restx import Namespace, Resource, cors

from api.schemas import response as res
from api.services import WorkIssuesService
from api.utils import auth
from api.utils.util import cors_preflight

API = Namespace("work-issues", description="Work Issues")


@cors_preflight("GET, POST")
@API.route("", methods=["GET", "POST", "OPTIONS"])
class WorkStatus(Resource):
    """Endpoint resource to manage work issues."""

    @staticmethod
    @cors.crossdomain(origin="*")
    @auth.require
    def get(work_id):
        """Return all active works."""
        works = WorkIssuesService.find_all_work_issues(work_id)
        return jsonify(res.WorkIssuesResponseSchema(many=True).dump(works)), HTTPStatus.OK