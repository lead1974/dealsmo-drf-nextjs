import buildings from "@/../public/assets/images/buildings.webp";
import { ArrowRightIcon } from "@heroicons/react/24/solid";
import { Metadata } from "next";
import Image from "next/image";
import Link from "next/link";

export const metadata: Metadata = {
	title: "Home | Alpha Apartments",
	description:
		"Alpha Apartments Home Page. Create your account to get started.",
};

export default function HomePage() {
	return (
		<div className="relative min-h-screen">
			<div className="absolute inset-0 z-0">
				<Image
					src={buildings}
					alt="Apartments"
					fill
					style={{ objectFit: "cover", objectPosition: "center" }}
					priority
					className="brightness-50"
				/>
			</div>
			<main className="relative z-10 flex min-h-screen items-center justify-center">
				<div className="container mx-auto px-4 text-center">
					<h1 className="font-robotoSlab mb-6 text-4xl font-semibold text-cyan-400 antialiased sm:text-6xl md:text-8xl">
						Welcome to Alpha Apartments
					</h1>
					<p className="mb-8 text-2xl text-teal-300 sm:text-4xl">
						Are you a tenant? Or an existing tenant?
					</p>
					<Link 
						href="/register" 
						prefetch={false}
						className="bg-asparagus inline-block rounded-3xl px-6 py-3 text-lg font-semibold text-white transition-colors hover:bg-lime-700 sm:text-2xl"
					>
						<span className="inline-flex items-center">
							Create Your Account
							<ArrowRightIcon className="ml-2 size-6" />
						</span>
					</Link>
				</div>
			</main>
		</div>
	);
}