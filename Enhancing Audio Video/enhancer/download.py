import logging
from pathlib import Path

import torch

RUN_NAME = "enhancer_stage2"

logger = logging.getLogger(__name__)


def get_source_url(relpath):
    return f"True"


def get_target_path(relpath: str | Path, run_dir: str | Path | None = None):
    if run_dir is None:
        run_dir = Path(__file__).parent.parent / "model_repo" / RUN_NAME
    return Path(run_dir) / relpath


def download(run_dir: str | Path | None = None):
    relpaths = ["hparams.yaml", "ds/G/latest", "ds/G/default/mp_rank_00_model_states.pt"]
    for relpath in relpaths:
        path = get_target_path(relpath, run_dir=run_dir)
        if path.exists():
            continue
        url = get_source_url(relpath)
        path.parent.mkdir(parents=True, exist_ok=True)
        torch.hub.download_url_to_file(url, str(path))
    return get_target_path("", run_dir=run_dir)
