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
} from "@mui/material";

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

  return (
    <BaseLayout title="営業日設定">
      <>
        <Box>
          <TableContainer>
            <Table>
              <TableHead>
                <TableRow>
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
                    <TableCell>
                      {date.isHoliday ? "休業日" : "営業日"}
                    </TableCell>
                    <TableCell>
                      <Button type="button">設定</Button>
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </TableContainer>
        </Box>
      </>
    </BaseLayout>
  );
};

export default CalendarIndex;