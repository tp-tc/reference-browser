# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from __future__ import absolute_import, print_function, unicode_literals

from importlib import import_module
from taskgraph.parameters import extend_parameters_schema

from .gradle import get_geckoview_version


def register(graph_config):
    """
    Import all modules that are siblings of this one, triggering decorators in
    the process.
    """
    _import_modules(["job", "worker_types", "routes", "target"])
    extend_parameters_schema(
        {
            Required("geckoview-version"): text_type,
            Required("gecko-revision"): text_type,
        }
    )


def _import_modules(modules):
    for module in modules:
        import_module(".{}".format(module), package=__name__)


def get_decision_parameters(graph_config, parameters):
    parameters["geckoview-version"] = get_geckoview_version()
    parameters["gecko-revision"] = "b74e5737da64a7af28ab4f81f996950917aa71c5"
