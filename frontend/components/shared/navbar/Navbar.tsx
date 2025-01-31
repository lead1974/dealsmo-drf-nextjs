import { HomeModernIcon } from "@heroicons/react/24/solid";
import Link from "next/link";
import ThemeSwitcher from "./ThemeSwitcher";
import MobileNavbar from "./MobileNavbar";

export default function Navbar() {
	return (
		<nav className="fixed z-50 w-full border-b-2 p-4 sm:p-6 lg:px-12 bg-baby_rich border-b-platinum shadow-platinum dark:border-b-0 dark:shadow-none">
			<div className="flex w-full items-center justify-between">
				<Link href="/" className="flex items-center">
					<HomeModernIcon className="mr-2 text-lime-500 size-11" />
					<p className="hidden h2-bold font-robotoSlab text-veryBlack dark:text-babyPowder sm:block">
						Alpha <span className="text-lime-500"> Apartments</span>
					</p>
				</Link>

				<div className="flex items-center gap-4 sm:gap-6 lg:gap-8">
					<ThemeSwitcher />
					<div className="block sm:hidden">
						<MobileNavbar />
					</div>
				</div>
			</div>
		</nav>
	);
}