import {
  Box,
  Table,
  TableBody,
  TableContainer,
  TableHead,
  TableRow,
  TableCell,
  Typography,
} from "@mui/material";
import BaseLayout from "@/components/BaseLayout";

type ReservationType = {
  reservationDate: string;
  name: string;
  email: string;
  phoneNumber: string;
};

const ReservationIndexPage = () => {
  const reservationData: ReservationType[] = [
    {
      reservationDate: "2024-10-01",
      name: "テスト太郎",
      email: "example@example.com",
      phoneNumber: "090-1234-5678",
    },
    {
      reservationDate: "2024-10-05",
      name: "テスト太郎2",
      email: "example2@example.com",
      phoneNumber: "090-1234-5678",
    },
    {
      reservationDate: "2024-10-10",
      name: "テスト太郎2",
      email: "example3@example.com",
      phoneNumber: "090-1234-5678",
    },
  ];

  return (
    <BaseLayout>
      <>
        <Typography>予約一覧</Typography>
        <Box>
          <TableContainer>
            <Table>
              <TableHead>
                <TableRow>
                  <TableCell>予約希望日</TableCell>
                  <TableCell>名前</TableCell>
                  <TableCell>メールアドレス</TableCell>
                  <TableCell>電話番号</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {reservationData.map((reservation) => (
                  <TableRow key={reservation.reservationDate}>
                    <TableCell>{reservation.reservationDate}</TableCell>
                    <TableCell>{reservation.name}</TableCell>
                    <TableCell>{reservation.email}</TableCell>
                    <TableCell>{reservation.phoneNumber}</TableCell>
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

export default ReservationIndexPage;
