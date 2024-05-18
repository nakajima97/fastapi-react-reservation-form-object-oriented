import camelcaseKeys from 'camelcase-keys';

const useReservationRepository = () => {
  const fetchReservations = async () => {
    const response = await fetch('http://localhost:8000/reservations');
    const data = await response.json();
    return camelcaseKeys(data.reservations);
  }

  return {
    fetchReservations
  }
}

export default useReservationRepository;