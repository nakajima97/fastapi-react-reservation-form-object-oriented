import camelcaseKeys from 'camelcase-keys';

import { ReservationType } from '../types';

const useReservationRepository = () => {
  const fetchReservations = async (): Promise<ReservationType[]> => {
    const response = await fetch('http://localhost:8000/reservations');
    const data = await response.json();
    return camelcaseKeys(data.reservations);
  }

  return {
    fetchReservations
  }
}

export default useReservationRepository;