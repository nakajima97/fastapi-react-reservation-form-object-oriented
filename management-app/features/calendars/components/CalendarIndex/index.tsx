"use client";

import BaseLayout from "@/components/BaseLayout";
import {
  Typography,
  Box,
  Table,
  TableContainer,
  TableHead,
  TableRow,
  TableCell,
  TableBody,
  Button,
  Checkbox,
  Select,
  MenuItem,
} from "@mui/material";
import { SelectChangeEvent } from "@mui/material/Select";

import { useState } from "react";
import SettingModal from "../SettingModal";
import AddCalendarDataDialog from "../AddCalendarDataDialog";

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

  // 1~12の数値の配列を作成する
  const createNumbers = (start: number, end: number) => {
    const numbers = [];
    for (let i = start; i <= end; i++) {
      numbers.push(i);
    }
    return numbers;
  };
  const months = createNumbers(1, 12);
  const years = createNumbers(2020, 2030);

  const [open, setOpen] = useState(false);
  const [isHoliday, setIsHoliday] = useState<boolean>(false);
  const [selectedMonth, setSelectedMonth] = useState<number>(1);
  const [selectedYear, setSelectedYear] = useState<number>(2024);
  const [isOpenedAddCalendarDialog, setIsOpenedAddCalendarDialog] =
    useState<boolean>(false);

  const handleChange = (event: SelectChangeEvent) => {
    setIsHoliday(stringToIsHoliday(event.target.value));
  };

  const handleChangeMonth = (event: SelectChangeEvent) => {
    setSelectedMonth(+event.target.value);
  };

  const handleChangeYear = (event: SelectChangeEvent) => {
    setSelectedYear(+event.target.value);
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
      <Box sx={{ display: "flex", gap: "10px", alignItems: "center" }}>
        <Select value={selectedYear.toString()} onChange={handleChangeYear}>
          {years.map((year) => (
            <MenuItem key={year} value={year}>
              {year}年
            </MenuItem>
          ))}
        </Select>
        <Select value={selectedMonth.toString()} onChange={handleChangeMonth}>
          {months.map((month) => (
            <MenuItem key={month} value={month}>
              {month}月
            </MenuItem>
          ))}
        </Select>
        <Button variant="contained">のカレンダーを表示する</Button>
      </Box>
      <Box sx={{ display: "flex", gap: "10px", alignItems: "center" }}>
        <Typography>選択した日付を</Typography>
        <Select value={isHolidayToString(isHoliday)} onChange={handleChange}>
          <MenuItem value="0">営業日に設定する</MenuItem>
          <MenuItem value="1">休日に設定する</MenuItem>
        </Select>
        <Button variant="contained">実行</Button>
      </Box>
      <Box>
        <TableContainer>
          <Table>
            <TableHead>
              <TableRow>
                <TableCell>一括選択</TableCell>
                <TableCell>日付</TableCell>
                <TableCell>曜日</TableCell>
                <TableCell>形態</TableCell>
                <TableCell>設定</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {monthDates.map((date) => (
                <TableRow key={date.date.toLocaleDateString()}>
                  <TableCell>
                    <Checkbox />
                  </TableCell>
                  <TableCell>
                    <Typography>
                      {date.date.getMonth() + 1}月{date.date.getDate()}日
                    </Typography>
                  </TableCell>
                  <TableCell>
                    <Typography>
                      {
                        ["日", "月", "火", "水", "木", "金", "土"][
                          date.date.getDay()
                        ]
                      }
                    </Typography>
                  </TableCell>
                  <TableCell>{date.isHoliday ? "休業日" : "営業日"}</TableCell>
                  <TableCell>
                    <Button type="button" onClick={() => setOpen(true)}>
                      設定
                    </Button>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
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
