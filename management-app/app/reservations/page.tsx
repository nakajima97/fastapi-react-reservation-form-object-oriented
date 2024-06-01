import ReservationIndexPage from "@/features/reservations/components/page";
import BaseLayout from "@/components/BaseLayout";

const Page = () => {
  return (
    <>
      <BaseLayout title="予約一覧">
        <ReservationIndexPage />
      </BaseLayout>
    </>
  );
};

export default Page;
