"use client";

import LoginPage from "@/features/login/components/LoginPage";
import { useRouter } from "next/navigation";

export default function Home() {
  const router = useRouter();

  const handleSubmit = () => {
    router.push("/reservations");
  };

  return (
    <main>
      <LoginPage handleSubmit={handleSubmit} />
    </main>
  );
}
