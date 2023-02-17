import os
import sys
from pathlib import Path

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(str(Path(SCRIPT_DIR).parent.parent))

from streamline.dataprep.data_process import DataProcessing


def run_cluster(argv):
    cv_train_path = argv[1]
    cv_test_path = argv[2]
    full_path = argv[3]
    scale_data = bool(argv[4])
    impute_data = bool(argv[5])
    multi_impute = bool(argv[6])
    overwrite_cv = bool(argv[7])
    class_label = argv[8] if argv[8] != "None" else None
    instance_label = argv[9] if argv[9] != "None" else None
    random_state = int(argv[10]) if argv[10] != "None" else None

    job_obj = DataProcessing(cv_train_path, cv_test_path,
                             full_path,
                             scale_data, impute_data, multi_impute, overwrite_cv,
                             class_label, instance_label, random_state)
    job_obj.run()


if __name__ == "__main__":
    sys.exit(run_cluster(sys.argv))