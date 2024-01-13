import { useEffect, useState } from "react";
import axios from "axios";
const people = [
  {
    name: "Lindsay Walton",
    title: "Front-end Developer",
    email: "lindsay.walton@example.com",
    role: "Member",
  },
  {
    name: "Lindsay Walton",
    title: "Front-end Developer",
    email: "lindsay.walton@example.com",
    role: "Member",
  },
  {
    name: "Lindsay Walton",
    title: "Front-end Developer",
    email: "lindsay.walton@example.com",
    role: "Member",
  },
  {
    name: "Lindsay Walton",
    title: "Front-end Developer",
    email: "lindsay.walton@example.com",
    role: "Member",
  },
  {
    name: "Lindsay Walton",
    title: "Front-end Developer",
    email: "lindsay.walton@example.com",
    role: "Member",
  },
  // More people...
];

export default function App() {
  const [url, setUrl] = useState("");

  const scrape_page = (e) => {
    e.preventDefault();
  };

  return (
    <div className="bg-white">
      <div className="relative isolate px-6 pt-14 lg:px-8">
        <div className="mx-auto max-w-2xl mt-20">
          <div className="text-center">
            <h1 className="text-4xl font-bold tracking-tight text-gray-900 sm:text-6xl">
              Yellow Pages Scraper
            </h1>
            <p className="mt-6 text-lg leading-8 text-gray-600">
              Paste the yellow pages url below to start generating leads for
              your business.
            </p>
            <div>
              <form className="mt-2 relative" onSubmit={scrape_page}>
                <input
                  type="text"
                  name="search"
                  id="search"
                  onChange={(e) => setUrl(e.target.value)}
                  className="block w-full mt-5 p-3 rounded-md border-0 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 outline-0 placeholder:text-gray-400 sm:text-sm sm:leading-6"
                  placeholder="Enter a yellow pages url"
                />
                <button className="absolute top-0 right-0 bg-[#FFDD04] font-semibold p-3 rounded-md">
                  Submit
                </button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
