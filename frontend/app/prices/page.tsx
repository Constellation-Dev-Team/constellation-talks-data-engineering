"use client";

import React, { useState, useEffect } from "react";
import api from "../db_connection";
import Select from "react-select";

interface Ticker {
  value: number;
  label: string;
}

const Prices: React.FC = () => {
  const [prices, setPrices] = useState([]);
  const [selectedTicker, setSelectedTicker] = useState<Ticker | null>();
  const [tickers, setTickers] = useState<Ticker[]>([]);


  return (
    <div className="container mx-auto p-4">
      <div className="mb-6 bg-slate-800 shadow-md rounded-lg p-6">
        <h1 className="text-3xl font-bold tracking-tight text-white">
          Prices
        </h1>
        </div>
        <div className="bg-white shadow-md rounded-lg p-6 mb-6">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <label
              htmlFor="prices"
              className="block text-sm font-medium text-gray-700 mb-2"
            >
              Prices
            </label>
            <Select
              value={selectedTicker}
              onChange={(selectedOption) => setSelectedTicker(selectedOption)}
              options={tickers}
              className="w-full"
              styles={{
                control: (styles) => ({
                  ...styles,
                  minHeight: "38px",
                }),
                option: (styles) => ({
                  ...styles,
                  backgroundColor: "white",
                  color: "black",
                  "&:hover": {
                    backgroundColor: "#3182ce",
                    color: "white",
                  },
                }),
              }}
            />
          </div>
        </div>
      </div>
    </div>
  );
};

export default Prices;
