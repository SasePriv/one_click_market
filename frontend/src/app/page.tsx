'use client'

import {Button} from "@nextui-org/button";
import { useState } from 'react';
import ThemeSwitcher from "@/shared/ThemeSwitcher";
import CardProduct from "@/shared/CardProduct";
import {Card, CardHeader, CardBody, CardFooter, Divider, Link, Image, Input} from "@nextui-org/react";
import { postSearch } from './api';

export default function Home() {
    const [search, setSearch] = useState('');
    const [items, setItems] = useState([])
    const [dataAnalysis, setDataAnalysis] = useState(null)
    const onSearchButton = async () => {
        try {
            const response = await postSearch({text: search});
            setItems(response.data['list_items'])
            setDataAnalysis({
                maxPrice: response.data['max_price'],
                minPrice: response.data['min_price'],
                averagePrice: response.data['average_price'],
            })
        } catch (e) {
            console.log(e)
        }
    }

    return (
        <div className="flex flex-center w-full justify-center content-center h-screen p-10">
            <Card className="max-w-[600px] w-full">
                <CardHeader className="flex gap-3 justify-between">
                    <Image
                        alt="nextui logo"
                        height={40}
                        radius="sm"
                        src="https://avatars.githubusercontent.com/u/86160567?s=200&v=4"
                        width={40}
                    />
                    <div className="flex flex-col justify-center">
                        <p className="text-md text-center">One Click Market</p>
                        <p className="text-small text-default-500 text-center">Peewi</p>
                    </div>
                    <ThemeSwitcher/>
                </CardHeader>
                <Divider/>
                <CardBody className="h-full">
                    <form>
                        <div className="flex gap-3 justify-center items-center">
                            <Input
                                value={search}
                                onChange={(e) => setSearch(e.target.value)}
                                size="sm"
                                type="text"
                                placeholder="Enter the name of item to search"
                            />
                            <Button onClick={onSearchButton} size="md" color="primary">Search</Button>
                        </div>
                    </form>
                    <div className="mt-3 flex flex-center flex-wrap justify-center gap-5">
                        { items.map((each, i) => <CardProduct key={i} product={each}/>) }
                    </div>
                </CardBody>
                <Divider/>
                <CardFooter className="h-20">
                    <div className="flex flex-col w-full my-3 ">
                        {dataAnalysis && <div className="flex w-full justify-center gap-4 mb-2">
                            <div>Max price: {dataAnalysis.maxPrice}$</div>
                            <div>Minium price: {dataAnalysis.minPrice}$</div>
                            <div>Average price: {dataAnalysis.averagePrice}$</div>
                        </div>}
                        <Link
                            isExternal
                            className="justify-center w-full"
                            showAnchorIcon
                            href="https://github.com/nextui-org/nextui"
                        >
                            <small>Visit source code on GitHub.</small>
                        </Link>
                    </div>
                </CardFooter>
            </Card>
            {/* <ThemeSwitcher /> */}
        </div>
    )
}
