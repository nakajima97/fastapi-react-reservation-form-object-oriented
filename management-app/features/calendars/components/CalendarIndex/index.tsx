"use client";

import { Typography, Box, Button, Select, MenuItem } from "@mui/material";
import { SelectChangeEvent } from "@mui/material/Select";

import { useState } from "react";
import SettingModal from "../SettingModal";
import AddCalendarDataDialog from "../AddCalendarDataDialog";
import CalendarTable from "../CalendarTable";
import SelectYearMonth from "../SelectYearMonth";

const CalendarIndex = () => {
  // 1ヶ月分の日付データを作成する
  const createMonthDates = () => {
    const dates = [];
    const date = new Date();
    const year = date.getFullYear();
    const month = date.getMonth();
    const lastDate = new Date(year, month + 1, 0).getDate();
    for (let i = 1; i <= lastDate; i++) {
      dates.push({ date: new Date(year, month, i), isHoliday: false });
    }
    return dates;
  };
  const monthDates = createMonthDates();

  const [open, setOpen] = useState(false);
  const [isHoliday, setIsHoliday] = useState<boolean>(false);

  const [isOpenedAddCalendarDialog, setIsOpenedAddCalendarDialog] =
    useState<boolean>(false);

  const handleChange = (event: SelectChangeEvent) => {
    setIsHoliday(stringToIsHoliday(event.target.value));
  };

  const isHolidayToString = (isHoliday: boolean) => {
    return isHoliday ? "1" : "0";
  };

  const stringToIsHoliday = (str: string) => {
    return str === "1" ? true : false;
  };

  return (
    <>
      <Box>
        <Button
          onClick={() => setIsOpenedAddCalendarDialog(true)}
          variant="contained"
        >
          日付データ追加
        </Button>
      </Box>
      <SelectYearMonth />
      <Box sx={{ display: "flex", gap: "10px", alignItems: "center" }}>
        <Typography>選択した日付を</Typography>
        <Select value={isHolidayToString(isHoliday)} onChange={handleChange}>
          <MenuItem value="0">営業日に設定する</MenuItem>
          <MenuItem value="1">休日に設定する</MenuItem>
        </Select>
        <Button variant="contained">実行</Button>
      </Box>
      <Box>
        <CalendarTable
          handleOpenSettingDialog={() => setOpen(true)}
          monthDates={monthDates}
        />
      </Box>
      <SettingModal open={open} onClose={() => setOpen(false)} />
      <AddCalendarDataDialog
        open={isOpenedAddCalendarDialog}
        onClose={() => setIsOpenedAddCalendarDialog(false)}
      />
    </>
  );
};

export default CalendarIndex;
