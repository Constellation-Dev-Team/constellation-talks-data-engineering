"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import React, { useState, useEffect } from "react";

const NavBar = () => {
  const router = useRouter();

  return (
    <nav className="bg-base-100 p-4">
      <div className="flex justify-between w-full">
        <div>
          <Link href="/" className="btn btn-ghost text-xl">
            Constellation
          </Link>
        </div>
        <div className="flex-grow flex justify-center space-x-4">
            <Link href="/prices" className="btn btn-ghost">
                Prices
            </Link>
            <Link href="/companies" className="btn btn-ghost">
                Companies
            </Link>
            <Link href="/studies" className="btn btn-ghost">
                Studies
            </Link>
            <Link href="/funds" className="btn btn-ghost">
                Funds
            </Link>
        </div>
      </div>
    </nav>
  );
};

export default NavBar;
