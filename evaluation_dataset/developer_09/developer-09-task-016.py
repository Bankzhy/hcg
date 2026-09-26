def extractHolidayDate(self, setting_holiday):
        ret = namedtuple("result", ["Holiday", "Month", "Day"])
        setting_holiday += 1
        ret.Holiday = str(setting_holiday)
        if (setting_holiday < 1) or (setting_holiday > Extents.Holidays):
            ekm_log("Out of bounds:  holiday " + str(setting_holiday))
            ret.Holiday = ret.Month = ret.Day = str(0)
            return ret
        idxday = "Holiday_" + str(setting_holiday) + "_Day"
        idxmon = "Holiday_" + str(setting_holiday) + "_Mon"
        if idxmon not in self.m_hldy:
            ret.Holiday = ret.Month = ret.Day = str(0)
            return ret
        if idxday not in self.m_hldy:
            ret.Holiday = ret.Month = ret.Day = str(0)
            return ret
        ret.Day = self.m_hldy[idxday][MeterData.StringValue]
        ret.Month = self.m_hldy[idxmon][MeterData.StringValue]
        return ret