import {
  Button,
  Checkbox,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Typography,
} from "@mui/material";

type Props = {
  handleOpenSettingDialog: () => void;
  monthDates: { date: Date; isHoliday: boolean }[];
};

const CalendarTable = ({ handleOpenSettingDialog, monthDates }: Props) => {
  return (
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
                <Button type="button" onClick={handleOpenSettingDialog}>
                  設定
                </Button>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

export default CalendarTable;
