import { HomeModernIcon } from "@heroicons/react/24/solid";
import Link from "next/link";
import ThemeSwitcher from "./ThemeSwitcher";

export default function Navbar() {
	return (
		<nav className="bg-baby_rich border-b-platinum shadow-platinum fixed z-50 flex w-full justify-between gap-5 border-b-2 p-4 sm:p-6 lg:px-12 dark:border-b-0 dark:shadow-none">
			<Link href="/" className="flex items-center">
				<HomeModernIcon className="mr-2 size-11 text-lime-500" />
				<p className="h2-bold font-robotoSlab text-veryBlack dark:text-babyPowder hidden sm:block">
					Alpha <span className="text-lime-500"> Apartments</span>
				</p>
			</Link>

			<div className="ml-auto flex items-center gap-4 sm:gap-6 lg:gap-8">
				<ThemeSwitcher />
				<div className="dark:text-pumpkin text-lg sm:text-xl">MobileNavbar</div>
			</div>
		</nav>
	);
}