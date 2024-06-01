import CalendarIndex from "@/features/calendars/components/CalendarIndex/index";
import BaseLayout from "@/components/BaseLayout";

const Page = () => {
  return (
    <>
      <BaseLayout title="営業日設定">
        <CalendarIndex />
      </BaseLayout>
    </>
  );
};

export default Page;
