import type { Metadata } from "next";
import { Inter } from "next/font/google"
import "./globals.css";
import NavBar from "./components/navbar";

const inter = Inter({subsets: ['latin']})


export const metadata: Metadata = {
  title: "Constellation",
  description: "Data engineering platform example",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" data-theme='synthwave'>
      <body className={inter.className}>
        <NavBar />
            {children}
      </body>
    </html>
  )
}
