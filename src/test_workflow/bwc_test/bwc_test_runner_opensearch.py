# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.

import logging
import os

from manifests.test_manifest import TestManifest
from test_workflow.bwc_test.bwc_test_runner import BwcTestRunner
from test_workflow.bwc_test.bwc_test_start_properties_opensearch import BwcTestStartPropertiesOpenSearch
from test_workflow.bwc_test.bwc_test_suite_opensearch import BwcTestSuiteOpenSearch
from test_workflow.test_args import TestArgs


class BwcTestRunnerOpenSearch(BwcTestRunner):

    def __init__(self, args: TestArgs, test_manifest: TestManifest):
        super().__init__(args, test_manifest)
        self.properties = BwcTestStartPropertiesOpenSearch(args.paths.get("opensearch", os.getcwd()))

        self.components = self.properties.build_manifest.components

        logging.info("Entering BWC test for OpenSearch")

    def __create_test_suite__(self, component, test_config, work_dir):
        return BwcTestSuiteOpenSearch(
            work_dir.name,
            component,
            test_config,
            self.test_recorder,
            self.properties.bundle_manifest,
        )
