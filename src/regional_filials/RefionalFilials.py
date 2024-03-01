class RegionalFilials:
    _RF: {
        'РФ Саратовский': 2
    }

    _MRF: {
        'МРФ Центр': 3
    }

    def get_regional_filial_id(self, regional_filial_name):
        return self.RF[regional_filial_name]

    def get_regional_filial_id(self, macro_regional_filial_name):
        return self.MRF[macro_regional_filial_name]

    def get_regional_filial_id(self):
        return 1
