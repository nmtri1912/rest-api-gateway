from ..common.resource_formatter import DataTrans
from ..common.exceptions import NotParseableException


class DataCommonTrans:
    resource_plural_name: str


class DataInTrans(DataCommonTrans, DataTrans):
    """
    General data transformer for ShipStation resource from channel to app
    """
    transform_singular: DataTrans

    def __call__(self, data):
        if self.resource_plural_name in data:
            result = list(map(self.transform_singular, data[self.resource_plural_name]))
        elif isinstance(data, dict):
            try:
                result = self.transform_singular(data)
            except KeyError:
                result = data
        elif 'errors' in data:
            result = data
        else:
            raise NotParseableException('Data not processed')
        return result


class DataOutTrans(DataTrans):
    """
    General data transformer for ShipStation resource from app to channel
    """
    transform_singular: DataTrans

    def __call__(self, data):
        if isinstance(data, list):
            result = list(map(self.transform_singular, data))
        elif isinstance(data, dict):
            result = self.transform_singular(data)
        else:
            raise NotParseableException('Data not processed')
        return result
