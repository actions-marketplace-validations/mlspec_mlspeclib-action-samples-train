from pathlib import Path
import os
import sys
import unittest
import subprocess

sys.path.append(str(Path.cwd()))
sys.path.append(str(Path.cwd() / "bin"))

from utils import setupLogger  # noqa


class DockerBuildTester(unittest.TestCase):
    def setUp(self):
        (self.rootLogger, self._buffer) = setupLogger()

    def test_docker_build(self):
        repo_name = os.environ.get(
            "INPUT_REPO_NAME", "mlspec"
        )
        container_name = os.environ.get(
            "INPUT_CONTAINER_NAME", "mlspeclib-action-samples-process-data"
        )
        exec_statement = ["docker", "run", f"{repo_name}/{container_name}:latest"]
        # p = subprocess.Popen(["docker"])
        # out, err = p.communicate()

        p = subprocess.Popen(
            exec_statement, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        out, err = p.communicate()
        self.rootLogger.debug(f"error = {str(err)}")
        self.assertTrue("ValueError" in str(err))


if __name__ == "__main__":
    unittest.main()
