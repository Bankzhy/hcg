def extractMonthTariff(self, month):
        ret = namedtuple("ret", ["Month", Field.kWh_Tariff_1, Field.kWh_Tariff_2, Field.kWh_Tariff_3,
                         Field.kWh_Tariff_4, Field.kWh_Tot, Field.Rev_kWh_Tariff_1,
                         Field.Rev_kWh_Tariff_2, Field.Rev_kWh_Tariff_3,
                         Field.Rev_kWh_Tariff_4, Field.Rev_kWh_Tot])
        month += 1
        ret.Month = str(month)
        if (month < 1) or (month > Extents.Months):
            ret.kWh_Tariff_1 = ret.kWh_Tariff_2 = ret.kWh_Tariff_3 = ret.kWh_Tariff_4 = str(0)
            ret.Rev_kWh_Tariff_1 = ret.Rev_kWh_Tariff_2 = ret.Rev_kWh_Tariff_3 = ret.Rev_kWh_Tariff_4 = str(0)
            ret.kWh_Tot = ret.Rev_kWh_Tot = str(0)
            ekm_log("Out of range(Extents.Months) month = " + str(month))
            return ret
        base_str = "Month_" + str(month) + "_"
        ret.kWh_Tariff_1 = self.m_mons[base_str + "Tariff_1"][MeterData.StringValue]
        ret.kWh_Tariff_2 = self.m_mons[base_str + "Tariff_2"][MeterData.StringValue]
        ret.kWh_Tariff_3 = self.m_mons[base_str + "Tariff_3"][MeterData.StringValue]
        ret.kWh_Tariff_4 = self.m_mons[base_str + "Tariff_4"][MeterData.StringValue]
        ret.kWh_Tot = self.m_mons[base_str + "Tot"][MeterData.StringValue]
        ret.Rev_kWh_Tariff_1 = self.m_rev_mons[base_str + "Tariff_1"][MeterData.StringValue]
        ret.Rev_kWh_Tariff_2 = self.m_rev_mons[base_str + "Tariff_2"][MeterData.StringValue]
        ret.Rev_kWh_Tariff_3 = self.m_rev_mons[base_str + "Tariff_3"][MeterData.StringValue]
        ret.Rev_kWh_Tariff_4 = self.m_rev_mons[base_str + "Tariff_4"][MeterData.StringValue]
        ret.Rev_kWh_Tot = self.m_rev_mons[base_str + "Tot"][MeterData.StringValue]
        return ret