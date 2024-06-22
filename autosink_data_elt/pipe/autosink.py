from autosink_data_elt.path.autosink import AutosinkPath, LOCAL_BACKEND
from autosink_data_elt.pipe.base import BasePipe
from autosink_data_elt.pipe.tools.unzip import unzip
from sparse_to_dense.cli.web import main


class LabelingPipe(BasePipe):

    def __init__(self) -> None:
        super().__init__()

    def __call__(self, directory_path):
        main(directory_path)


class ELTPipeBeforeLabeling(BasePipe):

    def __init__(self) -> None:
        super().__init__()

    def __call__(self, directory_path):
        """ 해야 하는 일들
        1. `volume/data-lake` 에서 `unzip()` 수행. -> 압축 해제 결과들이 `volume/data-lake/extract` 에 저장됨
        2. `volume/data-lake/extract` 내 모든 폴더들에 대해서 레이블링 파이프라인 실행
            2-1. 레이블링 파이프라인이 읽어갈 수 있는 형태로 셋업
                ???
            2-2. 
        """
        return unzip(directory_path)


class ELTPipeAfterLabeling(BasePipe):

    def __init__(self) -> None:
        super().__init__()

    def __call__(self):
        return super().__call__()


if __name__ == '__main__':
    autosink_path = AutosinkPath(
        backend=LOCAL_BACKEND,
        mount_dir='.',
        data_lake_rel_dir='data-lake',
        feature_store_rel_dir='feature-store',
    )
    pipe = ELTPipeBeforeLabeling()
    target_dir = pipe(autosink_path.data_lake_dir)
    pipe = LabelingPipe()
    pipe(target_dir)
    pipe = ELTPipeAfterLabeling()
    pipe()
