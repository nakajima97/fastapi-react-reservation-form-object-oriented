import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "予約管理",
  description: "予約を管理するアプリ",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="ja">
      <body>{children}</body>
    </html>
  );
}
