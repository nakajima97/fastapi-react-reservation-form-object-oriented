"use client";

import {
  Box,
  Table,
  TableBody,
  TableContainer,
  TableHead,
  TableRow,
  TableCell,
} from "@mui/material";
import BaseLayout from "@/components/BaseLayout";

import useReservationRepository from "../../hooks/useReservationRepository";
import { useEffect, useState } from "react";
import { ReservationType } from "../../types";

const ReservationIndexPage = () => {
  const [reservations, setReservations] = useState<ReservationType[]>([]);

  const { fetchReservations } = useReservationRepository();
  fetchReservations();

  useEffect(() => {
    (async () => {
      const data = await fetchReservations();
      setReservations(data);
    })();
  }, []);

  return (
    <BaseLayout title="予約一覧">
      <>
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
                {reservations.map((reservation) => (
                  <TableRow key={reservation.date}>
                    <TableCell>{reservation.date}</TableCell>
                    <TableCell>{reservation.name}</TableCell>
                    <TableCell>{reservation.emailAddress}</TableCell>
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
