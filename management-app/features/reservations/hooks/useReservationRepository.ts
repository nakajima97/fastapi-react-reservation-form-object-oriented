import camelcaseKeys from "camelcase-keys";

import { ReservationType } from "../types";
import { fetchData } from "../../../utils/fetch";

const useReservationRepository = () => {
  const fetchReservations = async (): Promise<ReservationType[]> => {
    return fetchData("http://localhost:8000/reservations");
  };

  return {
    fetchReservations,
  };
};

export default useReservationRepository;
