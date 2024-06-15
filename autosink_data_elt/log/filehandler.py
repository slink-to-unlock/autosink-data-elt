# 내장
import os
import json
import hashlib
import logging
import pytz
from datetime import datetime
from dataclasses import asdict
from collections import deque

# 프로젝트
from autosink_data_elt.log.template.dishwashing import *


def setup_logger():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    return logging.getLogger(__name__)


logger = setup_logger()


class JSONFileHandler:

    def __init__(self, user_id, timezone='Asia/Seoul'):
        self.user_id = user_id
        self.timezone = pytz.timezone(timezone)
        self.image_counter = 0
        self.dishwashing_id = self._generate_dishwashing_id()
        self.folder_name = self.dishwashing_id
        self.filename = os.path.join(self.folder_name, 'interactions.json')
        os.makedirs(self.folder_name, exist_ok=True)
        logger.info(
            f'Initialized JSONFileHandler with folder {self.folder_name} and file {self.filename}'
        )

    def _generate_dishwashing_id(self):
        hash_input = (self.user_id + str(datetime.now())).encode('utf-8')
        return hashlib.sha1(hash_input).hexdigest()[:10]

    def read_file(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                version = data.get('version', 1)
                if version == 1:
                    logger.info(
                        f'Read data with version 1 from {self.filename}')
                    return DishwashingDataV1(**data)
                elif version == 2:
                    logger.info(
                        f'Read data with version 2 from {self.filename}')
                    return DishwashingDataV2(**data)
                else:
                    logger.error(f'Unsupported version: {version}')
                    raise ValueError(f'Unsupported version: {version}')
        except FileNotFoundError:
            logger.error(f'File {self.filename} not found')
            raise
        except json.JSONDecodeError:
            logger.error(f'Error decoding JSON from file {self.filename}')
            raise

    def write_file(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data.to_dict(), file, indent=4)
        self.image_counter = 0  # Reset the image counter after writing to file
        logger.info(f'Wrote data to {self.filename} and reset image counter')

    def create_default_data(self,
                            dishwashing_start=None,
                            version=2,
                            deque_size=10):
        if dishwashing_start is None:
            dishwashing_start = datetime.now(
                self.timezone).isoformat(timespec='seconds')

        if version == 1:
            logger.info(f'Creating default data with version 1')
            return DishwashingDataV1(version=1,
                                     user_id=self.user_id,
                                     dishwashing_id=self.dishwashing_id,
                                     dishwashing_start=dishwashing_start)
        elif version == 2:
            logger.info(f'Creating default data with version 2')
            return DishwashingDataV2(version=2,
                                     user_id=self.user_id,
                                     dishwashing_id=self.dishwashing_id,
                                     dishwashing_start=dishwashing_start,
                                     interaction=deque(maxlen=deque_size))
        else:
            logger.error(f'Unsupported version: {version}')
            raise ValueError(f'Unsupported version: {version}')

    def add_interaction(self, data, **kwargs):
        timestamp = datetime.now().isoformat(timespec='seconds')
        # logger.info(f'Adding interaction with image from kwargs')

        if data.version == 1:
            interaction = InteractionV1.create(timestamp, kwargs.pop('image'),
                                               **kwargs)
        elif data.version == 2:
            interaction = InteractionV2.create(timestamp, kwargs.pop('image'),
                                               **kwargs)
        else:
            logger.error(f'Unsupported version: {data.version}')
            raise ValueError(f'Unsupported version: {data.version}')

        data.interaction.append(interaction)
        # logger.info(f'Added interaction: {interaction}')
        return data


if __name__ == '__main__':
    user_id = 'user1234'
    file_handler = JSONFileHandler(user_id)

    # 기본 데이터 생성 (버전 2)
    dishwashing_start = '2024-10-04T14:30:00'
    data = file_handler.create_default_data(dishwashing_start, version=2)

    # 상호작용 객체 생성 및 추가
    data = file_handler.add_interaction(data,
                                        model_output=0,
                                        arduino_output=0,
                                        magnetic_status=0)
    data = file_handler.add_interaction(data,
                                        model_output=0,
                                        arduino_output=0,
                                        magnetic_status=0)
    data = file_handler.add_interaction(data,
                                        model_output=0,
                                        arduino_output=1,
                                        magnetic_status=1)

    # 파일에 쓰기
    file_handler.write_file(data)

    # 파일에서 읽기
    read_data = file_handler.read_file()
    print(read_data)
